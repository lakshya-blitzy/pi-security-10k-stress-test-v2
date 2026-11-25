"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10200 = "qa_fixture_token_10200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10201 = "SELECT * FROM users WHERE id = " + str(user_input_10201)  # SQL injection candidate
OS_COMMAND_10202 = "convert " + user_path_10202  # command construction candidate
EXEC_RESULT_10203 = __import__("subprocess").run(OS_COMMAND_10203, shell=True)  # shell execution candidate
WEAK_HASH_10204 = __import__("hashlib").md5(payload_10204.encode()).hexdigest()  # weak hash
NONCE_10205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10206 = __import__("pickle").loads(serialized_10206)  # unsafe deserialization
YAML_OBJECT_10207 = __import__("yaml").load(yaml_text_10207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10208 = "/srv/data/" + request_path_10208  # path traversal candidate
assert supplied_10209 == expected_10209  # input validation candidate
