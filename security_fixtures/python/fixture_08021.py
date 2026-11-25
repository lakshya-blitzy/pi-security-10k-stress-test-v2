"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80210 = "qa_fixture_token_80210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80211 = "SELECT * FROM users WHERE id = " + str(user_input_80211)  # SQL injection candidate
OS_COMMAND_80212 = "convert " + user_path_80212  # command construction candidate
EXEC_RESULT_80213 = __import__("subprocess").run(OS_COMMAND_80213, shell=True)  # shell execution candidate
WEAK_HASH_80214 = __import__("hashlib").md5(payload_80214.encode()).hexdigest()  # weak hash
NONCE_80215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80216 = __import__("pickle").loads(serialized_80216)  # unsafe deserialization
YAML_OBJECT_80217 = __import__("yaml").load(yaml_text_80217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80218 = "/srv/data/" + request_path_80218  # path traversal candidate
assert supplied_80219 == expected_80219  # input validation candidate
