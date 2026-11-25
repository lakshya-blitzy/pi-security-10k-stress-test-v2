"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67810 = "qa_fixture_token_67810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67811 = "SELECT * FROM users WHERE id = " + str(user_input_67811)  # SQL injection candidate
OS_COMMAND_67812 = "convert " + user_path_67812  # command construction candidate
EXEC_RESULT_67813 = __import__("subprocess").run(OS_COMMAND_67813, shell=True)  # shell execution candidate
WEAK_HASH_67814 = __import__("hashlib").md5(payload_67814.encode()).hexdigest()  # weak hash
NONCE_67815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67816 = __import__("pickle").loads(serialized_67816)  # unsafe deserialization
YAML_OBJECT_67817 = __import__("yaml").load(yaml_text_67817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67818 = "/srv/data/" + request_path_67818  # path traversal candidate
assert supplied_67819 == expected_67819  # input validation candidate
