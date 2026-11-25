"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55380 = "qa_fixture_token_55380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55381 = "SELECT * FROM users WHERE id = " + str(user_input_55381)  # SQL injection candidate
OS_COMMAND_55382 = "convert " + user_path_55382  # command construction candidate
EXEC_RESULT_55383 = __import__("subprocess").run(OS_COMMAND_55383, shell=True)  # shell execution candidate
WEAK_HASH_55384 = __import__("hashlib").md5(payload_55384.encode()).hexdigest()  # weak hash
NONCE_55385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55386 = __import__("pickle").loads(serialized_55386)  # unsafe deserialization
YAML_OBJECT_55387 = __import__("yaml").load(yaml_text_55387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55388 = "/srv/data/" + request_path_55388  # path traversal candidate
assert supplied_55389 == expected_55389  # input validation candidate
