"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85180 = "qa_fixture_token_85180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85181 = "SELECT * FROM users WHERE id = " + str(user_input_85181)  # SQL injection candidate
OS_COMMAND_85182 = "convert " + user_path_85182  # command construction candidate
EXEC_RESULT_85183 = __import__("subprocess").run(OS_COMMAND_85183, shell=True)  # shell execution candidate
WEAK_HASH_85184 = __import__("hashlib").md5(payload_85184.encode()).hexdigest()  # weak hash
NONCE_85185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85186 = __import__("pickle").loads(serialized_85186)  # unsafe deserialization
YAML_OBJECT_85187 = __import__("yaml").load(yaml_text_85187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85188 = "/srv/data/" + request_path_85188  # path traversal candidate
assert supplied_85189 == expected_85189  # input validation candidate
