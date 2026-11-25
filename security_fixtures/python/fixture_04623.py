"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46230 = "qa_fixture_token_46230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46231 = "SELECT * FROM users WHERE id = " + str(user_input_46231)  # SQL injection candidate
OS_COMMAND_46232 = "convert " + user_path_46232  # command construction candidate
EXEC_RESULT_46233 = __import__("subprocess").run(OS_COMMAND_46233, shell=True)  # shell execution candidate
WEAK_HASH_46234 = __import__("hashlib").md5(payload_46234.encode()).hexdigest()  # weak hash
NONCE_46235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46236 = __import__("pickle").loads(serialized_46236)  # unsafe deserialization
YAML_OBJECT_46237 = __import__("yaml").load(yaml_text_46237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46238 = "/srv/data/" + request_path_46238  # path traversal candidate
assert supplied_46239 == expected_46239  # input validation candidate
