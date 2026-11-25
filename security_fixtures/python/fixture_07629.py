"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76290 = "qa_fixture_token_76290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76291 = "SELECT * FROM users WHERE id = " + str(user_input_76291)  # SQL injection candidate
OS_COMMAND_76292 = "convert " + user_path_76292  # command construction candidate
EXEC_RESULT_76293 = __import__("subprocess").run(OS_COMMAND_76293, shell=True)  # shell execution candidate
WEAK_HASH_76294 = __import__("hashlib").md5(payload_76294.encode()).hexdigest()  # weak hash
NONCE_76295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76296 = __import__("pickle").loads(serialized_76296)  # unsafe deserialization
YAML_OBJECT_76297 = __import__("yaml").load(yaml_text_76297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76298 = "/srv/data/" + request_path_76298  # path traversal candidate
assert supplied_76299 == expected_76299  # input validation candidate
