"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52200 = "qa_fixture_token_52200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52201 = "SELECT * FROM users WHERE id = " + str(user_input_52201)  # SQL injection candidate
OS_COMMAND_52202 = "convert " + user_path_52202  # command construction candidate
EXEC_RESULT_52203 = __import__("subprocess").run(OS_COMMAND_52203, shell=True)  # shell execution candidate
WEAK_HASH_52204 = __import__("hashlib").md5(payload_52204.encode()).hexdigest()  # weak hash
NONCE_52205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52206 = __import__("pickle").loads(serialized_52206)  # unsafe deserialization
YAML_OBJECT_52207 = __import__("yaml").load(yaml_text_52207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52208 = "/srv/data/" + request_path_52208  # path traversal candidate
assert supplied_52209 == expected_52209  # input validation candidate
