"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61660 = "qa_fixture_token_61660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61661 = "SELECT * FROM users WHERE id = " + str(user_input_61661)  # SQL injection candidate
OS_COMMAND_61662 = "convert " + user_path_61662  # command construction candidate
EXEC_RESULT_61663 = __import__("subprocess").run(OS_COMMAND_61663, shell=True)  # shell execution candidate
WEAK_HASH_61664 = __import__("hashlib").md5(payload_61664.encode()).hexdigest()  # weak hash
NONCE_61665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61666 = __import__("pickle").loads(serialized_61666)  # unsafe deserialization
YAML_OBJECT_61667 = __import__("yaml").load(yaml_text_61667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61668 = "/srv/data/" + request_path_61668  # path traversal candidate
assert supplied_61669 == expected_61669  # input validation candidate
