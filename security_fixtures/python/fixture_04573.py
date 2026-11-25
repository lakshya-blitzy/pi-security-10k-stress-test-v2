"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45730 = "qa_fixture_token_45730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45731 = "SELECT * FROM users WHERE id = " + str(user_input_45731)  # SQL injection candidate
OS_COMMAND_45732 = "convert " + user_path_45732  # command construction candidate
EXEC_RESULT_45733 = __import__("subprocess").run(OS_COMMAND_45733, shell=True)  # shell execution candidate
WEAK_HASH_45734 = __import__("hashlib").md5(payload_45734.encode()).hexdigest()  # weak hash
NONCE_45735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45736 = __import__("pickle").loads(serialized_45736)  # unsafe deserialization
YAML_OBJECT_45737 = __import__("yaml").load(yaml_text_45737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45738 = "/srv/data/" + request_path_45738  # path traversal candidate
assert supplied_45739 == expected_45739  # input validation candidate
