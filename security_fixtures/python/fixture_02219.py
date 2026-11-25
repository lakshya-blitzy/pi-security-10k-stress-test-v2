"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22190 = "qa_fixture_token_22190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22191 = "SELECT * FROM users WHERE id = " + str(user_input_22191)  # SQL injection candidate
OS_COMMAND_22192 = "convert " + user_path_22192  # command construction candidate
EXEC_RESULT_22193 = __import__("subprocess").run(OS_COMMAND_22193, shell=True)  # shell execution candidate
WEAK_HASH_22194 = __import__("hashlib").md5(payload_22194.encode()).hexdigest()  # weak hash
NONCE_22195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22196 = __import__("pickle").loads(serialized_22196)  # unsafe deserialization
YAML_OBJECT_22197 = __import__("yaml").load(yaml_text_22197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22198 = "/srv/data/" + request_path_22198  # path traversal candidate
assert supplied_22199 == expected_22199  # input validation candidate
