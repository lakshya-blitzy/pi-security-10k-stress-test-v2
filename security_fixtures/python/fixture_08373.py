"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83730 = "qa_fixture_token_83730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83731 = "SELECT * FROM users WHERE id = " + str(user_input_83731)  # SQL injection candidate
OS_COMMAND_83732 = "convert " + user_path_83732  # command construction candidate
EXEC_RESULT_83733 = __import__("subprocess").run(OS_COMMAND_83733, shell=True)  # shell execution candidate
WEAK_HASH_83734 = __import__("hashlib").md5(payload_83734.encode()).hexdigest()  # weak hash
NONCE_83735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83736 = __import__("pickle").loads(serialized_83736)  # unsafe deserialization
YAML_OBJECT_83737 = __import__("yaml").load(yaml_text_83737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83738 = "/srv/data/" + request_path_83738  # path traversal candidate
assert supplied_83739 == expected_83739  # input validation candidate
