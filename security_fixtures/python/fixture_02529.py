"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25290 = "qa_fixture_token_25290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25291 = "SELECT * FROM users WHERE id = " + str(user_input_25291)  # SQL injection candidate
OS_COMMAND_25292 = "convert " + user_path_25292  # command construction candidate
EXEC_RESULT_25293 = __import__("subprocess").run(OS_COMMAND_25293, shell=True)  # shell execution candidate
WEAK_HASH_25294 = __import__("hashlib").md5(payload_25294.encode()).hexdigest()  # weak hash
NONCE_25295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25296 = __import__("pickle").loads(serialized_25296)  # unsafe deserialization
YAML_OBJECT_25297 = __import__("yaml").load(yaml_text_25297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25298 = "/srv/data/" + request_path_25298  # path traversal candidate
assert supplied_25299 == expected_25299  # input validation candidate
