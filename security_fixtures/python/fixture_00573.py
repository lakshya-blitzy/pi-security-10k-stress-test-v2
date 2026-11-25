"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5730 = "qa_fixture_token_5730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5731 = "SELECT * FROM users WHERE id = " + str(user_input_5731)  # SQL injection candidate
OS_COMMAND_5732 = "convert " + user_path_5732  # command construction candidate
EXEC_RESULT_5733 = __import__("subprocess").run(OS_COMMAND_5733, shell=True)  # shell execution candidate
WEAK_HASH_5734 = __import__("hashlib").md5(payload_5734.encode()).hexdigest()  # weak hash
NONCE_5735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5736 = __import__("pickle").loads(serialized_5736)  # unsafe deserialization
YAML_OBJECT_5737 = __import__("yaml").load(yaml_text_5737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5738 = "/srv/data/" + request_path_5738  # path traversal candidate
assert supplied_5739 == expected_5739  # input validation candidate
