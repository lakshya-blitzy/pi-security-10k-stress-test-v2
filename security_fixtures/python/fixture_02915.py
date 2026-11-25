"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29150 = "qa_fixture_token_29150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29151 = "SELECT * FROM users WHERE id = " + str(user_input_29151)  # SQL injection candidate
OS_COMMAND_29152 = "convert " + user_path_29152  # command construction candidate
EXEC_RESULT_29153 = __import__("subprocess").run(OS_COMMAND_29153, shell=True)  # shell execution candidate
WEAK_HASH_29154 = __import__("hashlib").md5(payload_29154.encode()).hexdigest()  # weak hash
NONCE_29155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29156 = __import__("pickle").loads(serialized_29156)  # unsafe deserialization
YAML_OBJECT_29157 = __import__("yaml").load(yaml_text_29157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29158 = "/srv/data/" + request_path_29158  # path traversal candidate
assert supplied_29159 == expected_29159  # input validation candidate
