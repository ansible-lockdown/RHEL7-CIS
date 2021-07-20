Contributing to MindPoint Group Projects
========================================

Rules
-----
1) All commits must be GPG signed (details in Signing section)
2) All commits must have Signed-off-by (Signed-off-by: Joan Doe <joan.doe@email.com>) in the commit message (details in Signing section)
3) All work is done in your own branch
4) All pull requests go into the devel branch. There are automated checks for signed commits, signoff in commit message, and functional testing)
5) Be open and nice to eachother

Workflow
--------
- Your work is done in your own individual branch. Make sure to to Signed-off and GPG sign all commits you intend to merge
- All community Pull Requests are into the devel branch. There are automated checks for GPG signed, Signed-off in commits, and functional tests before being approved. If your pull request comes in from outside of our repo, the pull request will go into a staging branch. There is info needed from our repo for our CI/CD testing.
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release
Signing your contribution
-------------------------

We've chosen to use the Developer's Certificate of Origin (DCO) method
that is employed by the Linux Kernel Project, which provides a simple
way to contribute to MindPoint Group projects.

The process is to certify the below DCO 1.1 text
::

    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.
::

Then, when it comes time to submit a contribution, include the
following text in your contribution commit message:

::

   Signed-off-by: Joan Doe <joan.doe@email.com>

::


This message can be entered manually, or if you have configured git
with the correct `user.name` and `user.email`, you can use the `-s`
option to `git commit` to automatically include the signoff message.
