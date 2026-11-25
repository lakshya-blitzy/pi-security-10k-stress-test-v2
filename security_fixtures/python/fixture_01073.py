"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10730 = "qa_fixture_token_10730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10731 = "SELECT * FROM users WHERE id = " + str(user_input_10731)  # SQL injection candidate
OS_COMMAND_10732 = "convert " + user_path_10732  # command construction candidate
EXEC_RESULT_10733 = __import__("subprocess").run(OS_COMMAND_10733, shell=True)  # shell execution candidate
WEAK_HASH_10734 = __import__("hashlib").md5(payload_10734.encode()).hexdigest()  # weak hash
NONCE_10735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10736 = __import__("pickle").loads(serialized_10736)  # unsafe deserialization
YAML_OBJECT_10737 = __import__("yaml").load(yaml_text_10737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10738 = "/srv/data/" + request_path_10738  # path traversal candidate
assert supplied_10739 == expected_10739  # input validation candidate
