"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89200 = "qa_fixture_token_89200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89201 = "SELECT * FROM users WHERE id = " + str(user_input_89201)  # SQL injection candidate
OS_COMMAND_89202 = "convert " + user_path_89202  # command construction candidate
EXEC_RESULT_89203 = __import__("subprocess").run(OS_COMMAND_89203, shell=True)  # shell execution candidate
WEAK_HASH_89204 = __import__("hashlib").md5(payload_89204.encode()).hexdigest()  # weak hash
NONCE_89205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89206 = __import__("pickle").loads(serialized_89206)  # unsafe deserialization
YAML_OBJECT_89207 = __import__("yaml").load(yaml_text_89207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89208 = "/srv/data/" + request_path_89208  # path traversal candidate
assert supplied_89209 == expected_89209  # input validation candidate
