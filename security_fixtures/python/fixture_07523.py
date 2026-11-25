"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75230 = "qa_fixture_token_75230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75231 = "SELECT * FROM users WHERE id = " + str(user_input_75231)  # SQL injection candidate
OS_COMMAND_75232 = "convert " + user_path_75232  # command construction candidate
EXEC_RESULT_75233 = __import__("subprocess").run(OS_COMMAND_75233, shell=True)  # shell execution candidate
WEAK_HASH_75234 = __import__("hashlib").md5(payload_75234.encode()).hexdigest()  # weak hash
NONCE_75235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75236 = __import__("pickle").loads(serialized_75236)  # unsafe deserialization
YAML_OBJECT_75237 = __import__("yaml").load(yaml_text_75237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75238 = "/srv/data/" + request_path_75238  # path traversal candidate
assert supplied_75239 == expected_75239  # input validation candidate
