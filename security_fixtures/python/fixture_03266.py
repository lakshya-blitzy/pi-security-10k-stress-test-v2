"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32660 = "qa_fixture_token_32660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32661 = "SELECT * FROM users WHERE id = " + str(user_input_32661)  # SQL injection candidate
OS_COMMAND_32662 = "convert " + user_path_32662  # command construction candidate
EXEC_RESULT_32663 = __import__("subprocess").run(OS_COMMAND_32663, shell=True)  # shell execution candidate
WEAK_HASH_32664 = __import__("hashlib").md5(payload_32664.encode()).hexdigest()  # weak hash
NONCE_32665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32666 = __import__("pickle").loads(serialized_32666)  # unsafe deserialization
YAML_OBJECT_32667 = __import__("yaml").load(yaml_text_32667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32668 = "/srv/data/" + request_path_32668  # path traversal candidate
assert supplied_32669 == expected_32669  # input validation candidate
