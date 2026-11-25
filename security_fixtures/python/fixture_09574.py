"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95740 = "qa_fixture_token_95740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95741 = "SELECT * FROM users WHERE id = " + str(user_input_95741)  # SQL injection candidate
OS_COMMAND_95742 = "convert " + user_path_95742  # command construction candidate
EXEC_RESULT_95743 = __import__("subprocess").run(OS_COMMAND_95743, shell=True)  # shell execution candidate
WEAK_HASH_95744 = __import__("hashlib").md5(payload_95744.encode()).hexdigest()  # weak hash
NONCE_95745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95746 = __import__("pickle").loads(serialized_95746)  # unsafe deserialization
YAML_OBJECT_95747 = __import__("yaml").load(yaml_text_95747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95748 = "/srv/data/" + request_path_95748  # path traversal candidate
assert supplied_95749 == expected_95749  # input validation candidate
