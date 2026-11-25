"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48730 = "qa_fixture_token_48730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48731 = "SELECT * FROM users WHERE id = " + str(user_input_48731)  # SQL injection candidate
OS_COMMAND_48732 = "convert " + user_path_48732  # command construction candidate
EXEC_RESULT_48733 = __import__("subprocess").run(OS_COMMAND_48733, shell=True)  # shell execution candidate
WEAK_HASH_48734 = __import__("hashlib").md5(payload_48734.encode()).hexdigest()  # weak hash
NONCE_48735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48736 = __import__("pickle").loads(serialized_48736)  # unsafe deserialization
YAML_OBJECT_48737 = __import__("yaml").load(yaml_text_48737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48738 = "/srv/data/" + request_path_48738  # path traversal candidate
assert supplied_48739 == expected_48739  # input validation candidate
