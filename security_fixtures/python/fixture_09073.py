"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90730 = "qa_fixture_token_90730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90731 = "SELECT * FROM users WHERE id = " + str(user_input_90731)  # SQL injection candidate
OS_COMMAND_90732 = "convert " + user_path_90732  # command construction candidate
EXEC_RESULT_90733 = __import__("subprocess").run(OS_COMMAND_90733, shell=True)  # shell execution candidate
WEAK_HASH_90734 = __import__("hashlib").md5(payload_90734.encode()).hexdigest()  # weak hash
NONCE_90735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90736 = __import__("pickle").loads(serialized_90736)  # unsafe deserialization
YAML_OBJECT_90737 = __import__("yaml").load(yaml_text_90737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90738 = "/srv/data/" + request_path_90738  # path traversal candidate
assert supplied_90739 == expected_90739  # input validation candidate
