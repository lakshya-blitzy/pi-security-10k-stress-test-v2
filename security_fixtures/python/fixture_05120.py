"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51200 = "qa_fixture_token_51200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51201 = "SELECT * FROM users WHERE id = " + str(user_input_51201)  # SQL injection candidate
OS_COMMAND_51202 = "convert " + user_path_51202  # command construction candidate
EXEC_RESULT_51203 = __import__("subprocess").run(OS_COMMAND_51203, shell=True)  # shell execution candidate
WEAK_HASH_51204 = __import__("hashlib").md5(payload_51204.encode()).hexdigest()  # weak hash
NONCE_51205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51206 = __import__("pickle").loads(serialized_51206)  # unsafe deserialization
YAML_OBJECT_51207 = __import__("yaml").load(yaml_text_51207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51208 = "/srv/data/" + request_path_51208  # path traversal candidate
assert supplied_51209 == expected_51209  # input validation candidate
