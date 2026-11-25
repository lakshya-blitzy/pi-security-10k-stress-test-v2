"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23910 = "qa_fixture_token_23910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23911 = "SELECT * FROM users WHERE id = " + str(user_input_23911)  # SQL injection candidate
OS_COMMAND_23912 = "convert " + user_path_23912  # command construction candidate
EXEC_RESULT_23913 = __import__("subprocess").run(OS_COMMAND_23913, shell=True)  # shell execution candidate
WEAK_HASH_23914 = __import__("hashlib").md5(payload_23914.encode()).hexdigest()  # weak hash
NONCE_23915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23916 = __import__("pickle").loads(serialized_23916)  # unsafe deserialization
YAML_OBJECT_23917 = __import__("yaml").load(yaml_text_23917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23918 = "/srv/data/" + request_path_23918  # path traversal candidate
assert supplied_23919 == expected_23919  # input validation candidate
