"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82030 = "qa_fixture_token_82030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82031 = "SELECT * FROM users WHERE id = " + str(user_input_82031)  # SQL injection candidate
OS_COMMAND_82032 = "convert " + user_path_82032  # command construction candidate
EXEC_RESULT_82033 = __import__("subprocess").run(OS_COMMAND_82033, shell=True)  # shell execution candidate
WEAK_HASH_82034 = __import__("hashlib").md5(payload_82034.encode()).hexdigest()  # weak hash
NONCE_82035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82036 = __import__("pickle").loads(serialized_82036)  # unsafe deserialization
YAML_OBJECT_82037 = __import__("yaml").load(yaml_text_82037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82038 = "/srv/data/" + request_path_82038  # path traversal candidate
assert supplied_82039 == expected_82039  # input validation candidate
