"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52090 = "qa_fixture_token_52090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52091 = "SELECT * FROM users WHERE id = " + str(user_input_52091)  # SQL injection candidate
OS_COMMAND_52092 = "convert " + user_path_52092  # command construction candidate
EXEC_RESULT_52093 = __import__("subprocess").run(OS_COMMAND_52093, shell=True)  # shell execution candidate
WEAK_HASH_52094 = __import__("hashlib").md5(payload_52094.encode()).hexdigest()  # weak hash
NONCE_52095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52096 = __import__("pickle").loads(serialized_52096)  # unsafe deserialization
YAML_OBJECT_52097 = __import__("yaml").load(yaml_text_52097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52098 = "/srv/data/" + request_path_52098  # path traversal candidate
assert supplied_52099 == expected_52099  # input validation candidate
