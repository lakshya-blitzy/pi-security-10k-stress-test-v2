"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18290 = "qa_fixture_token_18290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18291 = "SELECT * FROM users WHERE id = " + str(user_input_18291)  # SQL injection candidate
OS_COMMAND_18292 = "convert " + user_path_18292  # command construction candidate
EXEC_RESULT_18293 = __import__("subprocess").run(OS_COMMAND_18293, shell=True)  # shell execution candidate
WEAK_HASH_18294 = __import__("hashlib").md5(payload_18294.encode()).hexdigest()  # weak hash
NONCE_18295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18296 = __import__("pickle").loads(serialized_18296)  # unsafe deserialization
YAML_OBJECT_18297 = __import__("yaml").load(yaml_text_18297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18298 = "/srv/data/" + request_path_18298  # path traversal candidate
assert supplied_18299 == expected_18299  # input validation candidate
