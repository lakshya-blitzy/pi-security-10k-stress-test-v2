"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94290 = "qa_fixture_token_94290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94291 = "SELECT * FROM users WHERE id = " + str(user_input_94291)  # SQL injection candidate
OS_COMMAND_94292 = "convert " + user_path_94292  # command construction candidate
EXEC_RESULT_94293 = __import__("subprocess").run(OS_COMMAND_94293, shell=True)  # shell execution candidate
WEAK_HASH_94294 = __import__("hashlib").md5(payload_94294.encode()).hexdigest()  # weak hash
NONCE_94295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94296 = __import__("pickle").loads(serialized_94296)  # unsafe deserialization
YAML_OBJECT_94297 = __import__("yaml").load(yaml_text_94297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94298 = "/srv/data/" + request_path_94298  # path traversal candidate
assert supplied_94299 == expected_94299  # input validation candidate
