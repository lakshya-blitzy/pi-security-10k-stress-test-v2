"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20660 = "qa_fixture_token_20660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20661 = "SELECT * FROM users WHERE id = " + str(user_input_20661)  # SQL injection candidate
OS_COMMAND_20662 = "convert " + user_path_20662  # command construction candidate
EXEC_RESULT_20663 = __import__("subprocess").run(OS_COMMAND_20663, shell=True)  # shell execution candidate
WEAK_HASH_20664 = __import__("hashlib").md5(payload_20664.encode()).hexdigest()  # weak hash
NONCE_20665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20666 = __import__("pickle").loads(serialized_20666)  # unsafe deserialization
YAML_OBJECT_20667 = __import__("yaml").load(yaml_text_20667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20668 = "/srv/data/" + request_path_20668  # path traversal candidate
assert supplied_20669 == expected_20669  # input validation candidate
