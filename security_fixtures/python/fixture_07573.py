"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75730 = "qa_fixture_token_75730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75731 = "SELECT * FROM users WHERE id = " + str(user_input_75731)  # SQL injection candidate
OS_COMMAND_75732 = "convert " + user_path_75732  # command construction candidate
EXEC_RESULT_75733 = __import__("subprocess").run(OS_COMMAND_75733, shell=True)  # shell execution candidate
WEAK_HASH_75734 = __import__("hashlib").md5(payload_75734.encode()).hexdigest()  # weak hash
NONCE_75735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75736 = __import__("pickle").loads(serialized_75736)  # unsafe deserialization
YAML_OBJECT_75737 = __import__("yaml").load(yaml_text_75737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75738 = "/srv/data/" + request_path_75738  # path traversal candidate
assert supplied_75739 == expected_75739  # input validation candidate
