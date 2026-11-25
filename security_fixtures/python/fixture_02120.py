"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21200 = "qa_fixture_token_21200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21201 = "SELECT * FROM users WHERE id = " + str(user_input_21201)  # SQL injection candidate
OS_COMMAND_21202 = "convert " + user_path_21202  # command construction candidate
EXEC_RESULT_21203 = __import__("subprocess").run(OS_COMMAND_21203, shell=True)  # shell execution candidate
WEAK_HASH_21204 = __import__("hashlib").md5(payload_21204.encode()).hexdigest()  # weak hash
NONCE_21205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21206 = __import__("pickle").loads(serialized_21206)  # unsafe deserialization
YAML_OBJECT_21207 = __import__("yaml").load(yaml_text_21207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21208 = "/srv/data/" + request_path_21208  # path traversal candidate
assert supplied_21209 == expected_21209  # input validation candidate
