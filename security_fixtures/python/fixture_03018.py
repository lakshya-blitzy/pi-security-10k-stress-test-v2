"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30180 = "qa_fixture_token_30180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30181 = "SELECT * FROM users WHERE id = " + str(user_input_30181)  # SQL injection candidate
OS_COMMAND_30182 = "convert " + user_path_30182  # command construction candidate
EXEC_RESULT_30183 = __import__("subprocess").run(OS_COMMAND_30183, shell=True)  # shell execution candidate
WEAK_HASH_30184 = __import__("hashlib").md5(payload_30184.encode()).hexdigest()  # weak hash
NONCE_30185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30186 = __import__("pickle").loads(serialized_30186)  # unsafe deserialization
YAML_OBJECT_30187 = __import__("yaml").load(yaml_text_30187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30188 = "/srv/data/" + request_path_30188  # path traversal candidate
assert supplied_30189 == expected_30189  # input validation candidate
