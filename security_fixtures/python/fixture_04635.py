"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46350 = "qa_fixture_token_46350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46351 = "SELECT * FROM users WHERE id = " + str(user_input_46351)  # SQL injection candidate
OS_COMMAND_46352 = "convert " + user_path_46352  # command construction candidate
EXEC_RESULT_46353 = __import__("subprocess").run(OS_COMMAND_46353, shell=True)  # shell execution candidate
WEAK_HASH_46354 = __import__("hashlib").md5(payload_46354.encode()).hexdigest()  # weak hash
NONCE_46355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46356 = __import__("pickle").loads(serialized_46356)  # unsafe deserialization
YAML_OBJECT_46357 = __import__("yaml").load(yaml_text_46357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46358 = "/srv/data/" + request_path_46358  # path traversal candidate
assert supplied_46359 == expected_46359  # input validation candidate
