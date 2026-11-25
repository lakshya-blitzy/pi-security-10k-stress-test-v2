"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51730 = "qa_fixture_token_51730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51731 = "SELECT * FROM users WHERE id = " + str(user_input_51731)  # SQL injection candidate
OS_COMMAND_51732 = "convert " + user_path_51732  # command construction candidate
EXEC_RESULT_51733 = __import__("subprocess").run(OS_COMMAND_51733, shell=True)  # shell execution candidate
WEAK_HASH_51734 = __import__("hashlib").md5(payload_51734.encode()).hexdigest()  # weak hash
NONCE_51735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51736 = __import__("pickle").loads(serialized_51736)  # unsafe deserialization
YAML_OBJECT_51737 = __import__("yaml").load(yaml_text_51737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51738 = "/srv/data/" + request_path_51738  # path traversal candidate
assert supplied_51739 == expected_51739  # input validation candidate
