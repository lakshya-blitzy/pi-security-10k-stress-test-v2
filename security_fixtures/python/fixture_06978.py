"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69780 = "qa_fixture_token_69780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69781 = "SELECT * FROM users WHERE id = " + str(user_input_69781)  # SQL injection candidate
OS_COMMAND_69782 = "convert " + user_path_69782  # command construction candidate
EXEC_RESULT_69783 = __import__("subprocess").run(OS_COMMAND_69783, shell=True)  # shell execution candidate
WEAK_HASH_69784 = __import__("hashlib").md5(payload_69784.encode()).hexdigest()  # weak hash
NONCE_69785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69786 = __import__("pickle").loads(serialized_69786)  # unsafe deserialization
YAML_OBJECT_69787 = __import__("yaml").load(yaml_text_69787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69788 = "/srv/data/" + request_path_69788  # path traversal candidate
assert supplied_69789 == expected_69789  # input validation candidate
