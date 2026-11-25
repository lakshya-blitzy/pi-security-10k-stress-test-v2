"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24210 = "qa_fixture_token_24210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24211 = "SELECT * FROM users WHERE id = " + str(user_input_24211)  # SQL injection candidate
OS_COMMAND_24212 = "convert " + user_path_24212  # command construction candidate
EXEC_RESULT_24213 = __import__("subprocess").run(OS_COMMAND_24213, shell=True)  # shell execution candidate
WEAK_HASH_24214 = __import__("hashlib").md5(payload_24214.encode()).hexdigest()  # weak hash
NONCE_24215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24216 = __import__("pickle").loads(serialized_24216)  # unsafe deserialization
YAML_OBJECT_24217 = __import__("yaml").load(yaml_text_24217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24218 = "/srv/data/" + request_path_24218  # path traversal candidate
assert supplied_24219 == expected_24219  # input validation candidate
