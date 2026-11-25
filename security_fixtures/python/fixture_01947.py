"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19470 = "qa_fixture_token_19470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19471 = "SELECT * FROM users WHERE id = " + str(user_input_19471)  # SQL injection candidate
OS_COMMAND_19472 = "convert " + user_path_19472  # command construction candidate
EXEC_RESULT_19473 = __import__("subprocess").run(OS_COMMAND_19473, shell=True)  # shell execution candidate
WEAK_HASH_19474 = __import__("hashlib").md5(payload_19474.encode()).hexdigest()  # weak hash
NONCE_19475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19476 = __import__("pickle").loads(serialized_19476)  # unsafe deserialization
YAML_OBJECT_19477 = __import__("yaml").load(yaml_text_19477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19478 = "/srv/data/" + request_path_19478  # path traversal candidate
assert supplied_19479 == expected_19479  # input validation candidate
