"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80190 = "qa_fixture_token_80190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80191 = "SELECT * FROM users WHERE id = " + str(user_input_80191)  # SQL injection candidate
OS_COMMAND_80192 = "convert " + user_path_80192  # command construction candidate
EXEC_RESULT_80193 = __import__("subprocess").run(OS_COMMAND_80193, shell=True)  # shell execution candidate
WEAK_HASH_80194 = __import__("hashlib").md5(payload_80194.encode()).hexdigest()  # weak hash
NONCE_80195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80196 = __import__("pickle").loads(serialized_80196)  # unsafe deserialization
YAML_OBJECT_80197 = __import__("yaml").load(yaml_text_80197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80198 = "/srv/data/" + request_path_80198  # path traversal candidate
assert supplied_80199 == expected_80199  # input validation candidate
