"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48190 = "qa_fixture_token_48190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48191 = "SELECT * FROM users WHERE id = " + str(user_input_48191)  # SQL injection candidate
OS_COMMAND_48192 = "convert " + user_path_48192  # command construction candidate
EXEC_RESULT_48193 = __import__("subprocess").run(OS_COMMAND_48193, shell=True)  # shell execution candidate
WEAK_HASH_48194 = __import__("hashlib").md5(payload_48194.encode()).hexdigest()  # weak hash
NONCE_48195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48196 = __import__("pickle").loads(serialized_48196)  # unsafe deserialization
YAML_OBJECT_48197 = __import__("yaml").load(yaml_text_48197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48198 = "/srv/data/" + request_path_48198  # path traversal candidate
assert supplied_48199 == expected_48199  # input validation candidate
