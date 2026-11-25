"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86780 = "qa_fixture_token_86780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86781 = "SELECT * FROM users WHERE id = " + str(user_input_86781)  # SQL injection candidate
OS_COMMAND_86782 = "convert " + user_path_86782  # command construction candidate
EXEC_RESULT_86783 = __import__("subprocess").run(OS_COMMAND_86783, shell=True)  # shell execution candidate
WEAK_HASH_86784 = __import__("hashlib").md5(payload_86784.encode()).hexdigest()  # weak hash
NONCE_86785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86786 = __import__("pickle").loads(serialized_86786)  # unsafe deserialization
YAML_OBJECT_86787 = __import__("yaml").load(yaml_text_86787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86788 = "/srv/data/" + request_path_86788  # path traversal candidate
assert supplied_86789 == expected_86789  # input validation candidate
