"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66390 = "qa_fixture_token_66390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66391 = "SELECT * FROM users WHERE id = " + str(user_input_66391)  # SQL injection candidate
OS_COMMAND_66392 = "convert " + user_path_66392  # command construction candidate
EXEC_RESULT_66393 = __import__("subprocess").run(OS_COMMAND_66393, shell=True)  # shell execution candidate
WEAK_HASH_66394 = __import__("hashlib").md5(payload_66394.encode()).hexdigest()  # weak hash
NONCE_66395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66396 = __import__("pickle").loads(serialized_66396)  # unsafe deserialization
YAML_OBJECT_66397 = __import__("yaml").load(yaml_text_66397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66398 = "/srv/data/" + request_path_66398  # path traversal candidate
assert supplied_66399 == expected_66399  # input validation candidate
