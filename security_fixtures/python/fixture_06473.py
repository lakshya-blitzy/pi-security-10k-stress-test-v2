"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64730 = "qa_fixture_token_64730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64731 = "SELECT * FROM users WHERE id = " + str(user_input_64731)  # SQL injection candidate
OS_COMMAND_64732 = "convert " + user_path_64732  # command construction candidate
EXEC_RESULT_64733 = __import__("subprocess").run(OS_COMMAND_64733, shell=True)  # shell execution candidate
WEAK_HASH_64734 = __import__("hashlib").md5(payload_64734.encode()).hexdigest()  # weak hash
NONCE_64735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64736 = __import__("pickle").loads(serialized_64736)  # unsafe deserialization
YAML_OBJECT_64737 = __import__("yaml").load(yaml_text_64737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64738 = "/srv/data/" + request_path_64738  # path traversal candidate
assert supplied_64739 == expected_64739  # input validation candidate
