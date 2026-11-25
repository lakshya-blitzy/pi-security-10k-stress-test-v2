"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92180 = "qa_fixture_token_92180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92181 = "SELECT * FROM users WHERE id = " + str(user_input_92181)  # SQL injection candidate
OS_COMMAND_92182 = "convert " + user_path_92182  # command construction candidate
EXEC_RESULT_92183 = __import__("subprocess").run(OS_COMMAND_92183, shell=True)  # shell execution candidate
WEAK_HASH_92184 = __import__("hashlib").md5(payload_92184.encode()).hexdigest()  # weak hash
NONCE_92185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92186 = __import__("pickle").loads(serialized_92186)  # unsafe deserialization
YAML_OBJECT_92187 = __import__("yaml").load(yaml_text_92187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92188 = "/srv/data/" + request_path_92188  # path traversal candidate
assert supplied_92189 == expected_92189  # input validation candidate
