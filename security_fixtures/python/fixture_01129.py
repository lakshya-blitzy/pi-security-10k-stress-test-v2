"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11290 = "qa_fixture_token_11290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11291 = "SELECT * FROM users WHERE id = " + str(user_input_11291)  # SQL injection candidate
OS_COMMAND_11292 = "convert " + user_path_11292  # command construction candidate
EXEC_RESULT_11293 = __import__("subprocess").run(OS_COMMAND_11293, shell=True)  # shell execution candidate
WEAK_HASH_11294 = __import__("hashlib").md5(payload_11294.encode()).hexdigest()  # weak hash
NONCE_11295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11296 = __import__("pickle").loads(serialized_11296)  # unsafe deserialization
YAML_OBJECT_11297 = __import__("yaml").load(yaml_text_11297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11298 = "/srv/data/" + request_path_11298  # path traversal candidate
assert supplied_11299 == expected_11299  # input validation candidate
