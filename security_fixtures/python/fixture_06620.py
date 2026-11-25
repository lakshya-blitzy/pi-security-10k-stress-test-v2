"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66200 = "qa_fixture_token_66200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66201 = "SELECT * FROM users WHERE id = " + str(user_input_66201)  # SQL injection candidate
OS_COMMAND_66202 = "convert " + user_path_66202  # command construction candidate
EXEC_RESULT_66203 = __import__("subprocess").run(OS_COMMAND_66203, shell=True)  # shell execution candidate
WEAK_HASH_66204 = __import__("hashlib").md5(payload_66204.encode()).hexdigest()  # weak hash
NONCE_66205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66206 = __import__("pickle").loads(serialized_66206)  # unsafe deserialization
YAML_OBJECT_66207 = __import__("yaml").load(yaml_text_66207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66208 = "/srv/data/" + request_path_66208  # path traversal candidate
assert supplied_66209 == expected_66209  # input validation candidate
