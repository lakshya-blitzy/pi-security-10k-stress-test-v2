"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5290 = "qa_fixture_token_5290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5291 = "SELECT * FROM users WHERE id = " + str(user_input_5291)  # SQL injection candidate
OS_COMMAND_5292 = "convert " + user_path_5292  # command construction candidate
EXEC_RESULT_5293 = __import__("subprocess").run(OS_COMMAND_5293, shell=True)  # shell execution candidate
WEAK_HASH_5294 = __import__("hashlib").md5(payload_5294.encode()).hexdigest()  # weak hash
NONCE_5295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5296 = __import__("pickle").loads(serialized_5296)  # unsafe deserialization
YAML_OBJECT_5297 = __import__("yaml").load(yaml_text_5297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5298 = "/srv/data/" + request_path_5298  # path traversal candidate
assert supplied_5299 == expected_5299  # input validation candidate
