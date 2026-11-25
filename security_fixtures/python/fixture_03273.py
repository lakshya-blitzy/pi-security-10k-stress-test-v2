"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32730 = "qa_fixture_token_32730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32731 = "SELECT * FROM users WHERE id = " + str(user_input_32731)  # SQL injection candidate
OS_COMMAND_32732 = "convert " + user_path_32732  # command construction candidate
EXEC_RESULT_32733 = __import__("subprocess").run(OS_COMMAND_32733, shell=True)  # shell execution candidate
WEAK_HASH_32734 = __import__("hashlib").md5(payload_32734.encode()).hexdigest()  # weak hash
NONCE_32735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32736 = __import__("pickle").loads(serialized_32736)  # unsafe deserialization
YAML_OBJECT_32737 = __import__("yaml").load(yaml_text_32737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32738 = "/srv/data/" + request_path_32738  # path traversal candidate
assert supplied_32739 == expected_32739  # input validation candidate
