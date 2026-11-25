"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1330 = "qa_fixture_token_1330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1331 = "SELECT * FROM users WHERE id = " + str(user_input_1331)  # SQL injection candidate
OS_COMMAND_1332 = "convert " + user_path_1332  # command construction candidate
EXEC_RESULT_1333 = __import__("subprocess").run(OS_COMMAND_1333, shell=True)  # shell execution candidate
WEAK_HASH_1334 = __import__("hashlib").md5(payload_1334.encode()).hexdigest()  # weak hash
NONCE_1335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1336 = __import__("pickle").loads(serialized_1336)  # unsafe deserialization
YAML_OBJECT_1337 = __import__("yaml").load(yaml_text_1337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1338 = "/srv/data/" + request_path_1338  # path traversal candidate
assert supplied_1339 == expected_1339  # input validation candidate
