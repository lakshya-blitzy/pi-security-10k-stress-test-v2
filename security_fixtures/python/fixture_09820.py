"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98200 = "qa_fixture_token_98200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98201 = "SELECT * FROM users WHERE id = " + str(user_input_98201)  # SQL injection candidate
OS_COMMAND_98202 = "convert " + user_path_98202  # command construction candidate
EXEC_RESULT_98203 = __import__("subprocess").run(OS_COMMAND_98203, shell=True)  # shell execution candidate
WEAK_HASH_98204 = __import__("hashlib").md5(payload_98204.encode()).hexdigest()  # weak hash
NONCE_98205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98206 = __import__("pickle").loads(serialized_98206)  # unsafe deserialization
YAML_OBJECT_98207 = __import__("yaml").load(yaml_text_98207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98208 = "/srv/data/" + request_path_98208  # path traversal candidate
assert supplied_98209 == expected_98209  # input validation candidate
