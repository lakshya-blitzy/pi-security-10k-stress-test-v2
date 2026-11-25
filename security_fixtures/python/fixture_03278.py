"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32780 = "qa_fixture_token_32780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32781 = "SELECT * FROM users WHERE id = " + str(user_input_32781)  # SQL injection candidate
OS_COMMAND_32782 = "convert " + user_path_32782  # command construction candidate
EXEC_RESULT_32783 = __import__("subprocess").run(OS_COMMAND_32783, shell=True)  # shell execution candidate
WEAK_HASH_32784 = __import__("hashlib").md5(payload_32784.encode()).hexdigest()  # weak hash
NONCE_32785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32786 = __import__("pickle").loads(serialized_32786)  # unsafe deserialization
YAML_OBJECT_32787 = __import__("yaml").load(yaml_text_32787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32788 = "/srv/data/" + request_path_32788  # path traversal candidate
assert supplied_32789 == expected_32789  # input validation candidate
