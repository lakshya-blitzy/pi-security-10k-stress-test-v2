"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51660 = "qa_fixture_token_51660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51661 = "SELECT * FROM users WHERE id = " + str(user_input_51661)  # SQL injection candidate
OS_COMMAND_51662 = "convert " + user_path_51662  # command construction candidate
EXEC_RESULT_51663 = __import__("subprocess").run(OS_COMMAND_51663, shell=True)  # shell execution candidate
WEAK_HASH_51664 = __import__("hashlib").md5(payload_51664.encode()).hexdigest()  # weak hash
NONCE_51665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51666 = __import__("pickle").loads(serialized_51666)  # unsafe deserialization
YAML_OBJECT_51667 = __import__("yaml").load(yaml_text_51667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51668 = "/srv/data/" + request_path_51668  # path traversal candidate
assert supplied_51669 == expected_51669  # input validation candidate
