"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24280 = "qa_fixture_token_24280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24281 = "SELECT * FROM users WHERE id = " + str(user_input_24281)  # SQL injection candidate
OS_COMMAND_24282 = "convert " + user_path_24282  # command construction candidate
EXEC_RESULT_24283 = __import__("subprocess").run(OS_COMMAND_24283, shell=True)  # shell execution candidate
WEAK_HASH_24284 = __import__("hashlib").md5(payload_24284.encode()).hexdigest()  # weak hash
NONCE_24285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24286 = __import__("pickle").loads(serialized_24286)  # unsafe deserialization
YAML_OBJECT_24287 = __import__("yaml").load(yaml_text_24287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24288 = "/srv/data/" + request_path_24288  # path traversal candidate
assert supplied_24289 == expected_24289  # input validation candidate
